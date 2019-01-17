package uasir;

import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class crawler {
    static String sinopsis;
    static koneksi conn= new koneksi();
     
    public void get(){
        try {
            Document doc = Jsoup.connect("https://www.komikindo.tv/manga/").get();      // connecting web
            Elements body = doc.select("div#wrapper");                                  // fokus data pada bagian body
            
            for (Element step: body.select("div.utao")){                            
                String method=step.select("div.uta div.luf a").attr("href");            // pengambilan data link
                String method1=step.select("div.uta div.luf a").attr("title");          // pengambilan judul
//                System.out.println("titel : "+method1);
                String method2=step.select("div.uta div.luf span.gee").text();          // pengambilan genre
//                System.out.println("genre : "+method2);
                scrap(method);
                input(method1,method2, sinopsis);                                       // input data to table komik
                String[] kataKata = splitKalimat(sinopsis);                             // input data to table unik
                for (String kata : kataKata) {
                    unik(kata);
                }
            }
            
                  } catch (IOException ex) {
            Logger.getLogger(crawler.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
    static void scrap(String a){                                                        //mengambil bagian sinopsis
        try {
            Document docu = Jsoup.connect(a).get();
            Elements body = docu.select("div#wrapper");
            
            for (Element scrap: body.select("div.infx")){
                sinopsis=scrap.select("div.rm span p").text();                          //pengambilan data sinopsis
            }
           
                  } catch (IOException ex) {
            Logger.getLogger(crawler.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
    public static void input(String judul,String genre, String sinopsis){
        String sql="insert into komik "+
	"values"+
	"('"+judul+"', "+
	"'"+genre+"', "+
        "'"+sinopsis+"'"+
	")";
        conn.simpanData(sql);
    }
    
    public static void unik(String kata){
        String sql="insert into kata_unik "+
	"values"+
	"('"+kata+"'"+
	")";
        conn.simpanData(sql);
    }
    
    static String[] splitKalimat(String kalimat) {
    return kalimat.split(" ");
  }
    
}
