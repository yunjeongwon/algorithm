import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int N1, N2;
    static String G1, G2;
    static ArrayList<Po> arrList = new ArrayList<>();
    static int T;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N1 = Integer.parseInt(st.nextToken());
        N2 = Integer.parseInt(st.nextToken());
        G1 = br.readLine();
        G2 = br.readLine();
        st = new StringTokenizer(br.readLine());
        T = Integer.parseInt(st.nextToken());

        for (int i = G1.length() - 1; i > -1; i--) {
            arrList.add(new Po(G1.charAt(i), 1));
        }
        for (int i = 0; i < G2.length(); i++) {
            arrList.add(new Po(G2.charAt(i), -1));
        }
        for (int t = 0; t < T; t++) {
            int k = 0;
            while (k < arrList.size() - 1) {
                if (arrList.get(k).dic == 1 && arrList.get(k + 1).dic == -1) {
                    Po cur = arrList.get(k);
                    Po next = arrList.get(k + 1);
                    arrList.set(k, next);
                    arrList.set(k + 1, cur);
                    k++;
                }
                k++;
            }
        }
        for (int i = 0; i < arrList.size(); i++) {
            System.out.print(arrList.get(i).ch);
        }
        System.out.println();
    }
    public static class Po {
        char ch;
        int dic;
        public Po (char ch, int dic) {
            this.ch = ch;
            this.dic = dic;
        }
    }
}
