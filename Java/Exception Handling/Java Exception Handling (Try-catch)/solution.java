import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        try{
            int x = s.nextInt();
            int y = s.nextInt();
            System.out.print(x/y);
        }
        catch(InputMismatchException e){
            System.out.print("java.util.InputMismatchException");
        }
        catch(Exception e){
            System.out.print(e);
        }
    }
}
