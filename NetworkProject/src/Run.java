import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Scanner;
import org.apache.commons.net.whois.WhoisClient;

public class Run {

	public static void main(String[] args) throws IOException, InterruptedException {
		
			
		// Preparing file reader 
		String dir = "/home/cobit/Downloads/TLSprobing-master/GeoIPASNum2.csv";
		FileInputStream inputStream = new FileInputStream(new File(dir));
		Scanner reader = new Scanner(inputStream, "UTF-8");		

        String keyword = "University of Utah";
        
        ArrayList<String> list = new ArrayList<>();
        int index = 0;
        // Iterating on lines of GeoIPNum file 
        while(reader.hasNext()){
            String line = reader.nextLine();
            String[] tokens = line.split(",");
            
            // if found 
            if(tokens[2].toLowerCase().contains(keyword.toLowerCase())) {
            	System.out.println(tokens[2]);
            	String temp = tokens[2];
            	temp = temp.substring(1, temp.length()-1);
            	String[] temp_tokens = temp.split(" ");
            	//System.out.println(temp_tokens[0]);
            	if( !list.contains(temp_tokens[0]) )
            		list.add(temp_tokens[0]);
            }       
            index++;	
            	
        }
        
        //list.remove("AS13712");
        
        System.out.println("Found AS list for keyword: " + keyword + "\n" + list);
        //String command = "whois -h whois.radb.net -- \'-i origin "+ list.get(0)+"\' | grep -Eo \"([0-9.]+){4}/[0-9]+\"";
        //System.out.println(command + "\n");
        
        String outFile = keyword+".txt";
		PrintWriter writer = new PrintWriter(outFile, "UTF-8");
        
		for(int j=0; j<list.size(); j++){ // iterating on list of AS numbers 
        
			// whois queriying
	        String command2 = "-i origin " + list.get(j);
	    	StringBuilder result = new StringBuilder("");    	
			WhoisClient whois = new WhoisClient();
			try {
				whois.connect("whois.radb.net");
				String whoisData = whois.query(command2);
				result.append(whoisData);
				whois.disconnect();
	
			}  catch (IOException e) {
				e.printStackTrace();
			}		
			
			// regex spliting router IP addresses 
			String[] lines = result.toString().split("\n");
			ArrayList<String> subnet_list = new ArrayList<>();
			for(int i=0; i<lines.length ; i++){
				if(lines[i].contains("route:")){
					String add_subnet = lines[i].substring(7).trim();
					if(!subnet_list.contains(add_subnet)){ //duplicate checker
						System.out.println(add_subnet);
						subnet_list.add(add_subnet);
						writer.println(add_subnet);
					}
				
				}				
			}
			
		}
		
		writer.close();

		
	}

}