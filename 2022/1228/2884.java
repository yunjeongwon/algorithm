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
        StringTokenizer st = new StringTokenizer(br.readLine());
        int H = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        if (M >= 45) {
            M -= 45;
        } else {
            H -= 1;
            M += 15;
        }
        if (H == -1) {
            H = 23;
        }
        System.out.print(H);
        System.out.print(" ");
        System.out.print(M);
        System.out.println();
    }
}
