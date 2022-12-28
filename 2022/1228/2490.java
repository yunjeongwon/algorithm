import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        String a = br.readLine();
//        System.out.println(a);
//        System.out.println("Hello world!!");

//        Scanner sc = new Scanner(System.in);
//        String s = sc.next();
//        System.out.println(s);
//        sc.close();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < 3; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int cnt = 0;
            for (int k = 0; k < 4; k++) {
                if (Integer.parseInt(st.nextToken()) == 0) {
                    cnt++;
                }
            }
            switch (cnt) {
                case 0:
                    System.out.println('E');
                    break;
                case 1:
                    System.out.println('A');
                    break;
                case 2:
                    System.out.println('B');
                    break;
                case 3:
                    System.out.println('C');
                    break;
                case 4:
                    System.out.println('D');
                    break;
            }
        }
    }
}
