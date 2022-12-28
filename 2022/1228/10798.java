import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static ArrayList<String> arrList = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 5; i++) {
            arrList.add(br.readLine());
        }
        String ans = "";
        for (int k = 0; k < 15; k++) {
            for (int i = 0; i < 5; i++) {
                if (arrList.get(i).length() > k) {
                    ans += arrList.get(i).charAt(k);
                }
            }
        }
        System.out.println(ans);
    }
}
