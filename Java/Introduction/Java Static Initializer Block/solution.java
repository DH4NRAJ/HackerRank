import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

static Scanner s = new Scanner(System.in);
static int B = s.nextInt();
static int H = s.nextInt();
static boolean flag = (B>0)&&(H>0);
static {
  if(!flag){
  System.out.println("java.lang.Exception: Breadth and height must be positive");
  }
}

public static void main(String[] args){
		if(flag){
			int area=B*H;
			System.out.print(area);
		}
		
	}//end of main

}//end of class
