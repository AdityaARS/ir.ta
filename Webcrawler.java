package webcrawler;

import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class Webcrawler {
    public static void main(String[] args) {
        
        try {
            Document doc = Jsoup.connect("https://www.komikindo.tv/manga/").get();  // connecting web
            Elements body = doc.select("div#wrapper");                              // fokus data pada bagian body
            
            for (Element step: body.select("div.utao")){                            
                String method=step.select("div.uta div.luf a").attr("href");        // pengambilan data link
                scrap(method);
                String method1=step.select("div.uta div.luf a").attr("title");       //pengambilan judul
//                System.out.println("titel : "+method1);
                String method2=step.select("div.uta div.luf span.gee").text();       //pengambilan genre
//                System.out.println("genre : "+method2);
            }
           
                  } catch (IOException ex) {
            Logger.getLogger(Webcrawler.class.getName()).log(Level.SEVERE, null, ex);
        }
        
    }
    
    static void scrap(String a){ //mengambil bagian sinopsis
        try {
            Document docu = Jsoup.connect(a).get();
            Elements body = docu.select("div#wrapper");
            
            for (Element scrap: body.select("div.infx")){
                String sinopsis=scrap.select("div.rm span p").text();              //pengambilan data sinopsis
                
                System.out.println("");
                System.out.println("sinopsis : ");
                System.out.println(sinopsis);
            }
           
                  } catch (IOException ex) {
            Logger.getLogger(Webcrawler.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
}
