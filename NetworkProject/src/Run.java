import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Scanner;
import org.apache.commons.net.whois.WhoisClient;

public class Run {

	public static void main(String[] args) throws IOException, InterruptedException {
		
			
		// Preparing file reader 
		String dir = "/home/cobit/Downloads/TLSprobing-master/GeoIPASNum2.csv";
		FileInputStream inputStream = new FileInputStream(new File(dir));
		Scanner reader = new Scanner(inputStream, "UTF-8");		

        String keyword = "Irvine";
        
        ArrayList<String> list = new ArrayList<>();
        int index = 0;
        // Iterating on lines of GeoIPNum file 
        while(reader.hasNext()){
            String line = reader.nextLine();
            String[] tokens = line.split(",");
            
            // if found 
            if(tokens[2].contains(keyword)){
            	String temp = tokens[2];
            	temp = temp.substring(1, temp.length()-1);
            	String[] temp_tokens = temp.split(" ");
            	//System.out.println(temp_tokens[0]);
            	if( !list.contains(temp_tokens[0]) )
            		list.add(temp_tokens[0]);
            }       
            index++;	
            	
        }
		
        System.out.println("Found AS list for keyword: " + keyword + "\n" + list);
        String command = "whois -h whois.radb.net -- \'-i origin AS5693\' | grep -Eo \"([0-9.]+){4}/[0-9]+\"";
        String[] commands = {"whois","-h whois.radb.net","-i origin AS5693", "grep -Eo \"([0-9.]+){4}/[0-9]+\""};
        System.out.println(command);
        final Process p = Runtime.getRuntime().exec(commands);

        new Thread(new Runnable() {
            public void run() {
             BufferedReader input = new BufferedReader(new InputStreamReader(p.getInputStream()));
             String line = null; 

             try {
                while ((line = input.readLine()) != null)
                    System.out.println(line);
             } catch (IOException e) {
                    e.printStackTrace();
             }
            }
        }).start();

        p.waitFor();
        
    	StringBuilder result = new StringBuilder("");

    	String command2 = "whois -h whois.arin.net -i origin AS5693";
		WhoisClient whois = new WhoisClient();
		try {

			//default is internic.net
			whois.connect("whois.radb.net");
			//whois.connect("whois.radb.net");
			
			String whoisData1 = whois.query(command2);
			result.append(whoisData1);
			whois.disconnect();

		}  catch (IOException e) {
			e.printStackTrace();
		}
		System.out.println(result);
		
		
		
	}

}
