import java.util.*;
import java.io.*;

class MultiTap{

  public String multiTapEncode(String input){
      Hashtable<String,String> encodeDictionary = multiTapCreateEncodeDictionary();
      String c;
      input = input.toUpperCase();
      String plaintext = "";
      for(int i= 0;i<input.length();i++){
          if(input.charAt(i) != ' ')
              plaintext += input.charAt(i);
      }
      String ciphertext = "";
      for(int i=0;i<plaintext.length();++i){
          ciphertext += encodeDictionary.get(Character.toString(plaintext.charAt(i)));
          if(i!=plaintext.length())
              ciphertext += "-";
      }
      return ciphertext.substring(0,ciphertext.length()-1);
  }

  public String multiTapDecode(String ciphertext,String delimiter){
      Hashtable<String,String> decodeDictionary = multiTapCreateDecodeDictionary();
      String[] ciphertextArray = ciphertext.split(delimiter);
      String plaintext = "";
      for(int i=0;i<ciphertextArray.length;i++){
          plaintext += decodeDictionary.get(ciphertextArray[i]);
      }
      return plaintext;
  }



  public Hashtable<String,String> multiTapCreateEncodeDictionary(){
      Hashtable <String,String> encodeDictionary = new Hashtable<String,String>();
      encodeDictionary.put("A","2");
      encodeDictionary.put("B","22");
      encodeDictionary.put("C","222");
      encodeDictionary.put("D","3");
      encodeDictionary.put("E","33");
      encodeDictionary.put("F","333");
      encodeDictionary.put("G","4");
      encodeDictionary.put("H","44");
      encodeDictionary.put("I","444");
      encodeDictionary.put("J","5");
      encodeDictionary.put("K","55");
      encodeDictionary.put("L","555");
      encodeDictionary.put("M","6");
      encodeDictionary.put("N","66");
      encodeDictionary.put("O","666");
      encodeDictionary.put("P","7");
      encodeDictionary.put("Q","77");
      encodeDictionary.put("R","777");
      encodeDictionary.put("S","7777");
      encodeDictionary.put("T","8");
      encodeDictionary.put("U","88");
      encodeDictionary.put("V","888");
      encodeDictionary.put("W","9");
      encodeDictionary.put("X","99");
      encodeDictionary.put("Y","999");
      encodeDictionary.put("Z","9999");
      encodeDictionary.put(" "," ");
      return encodeDictionary;
  }




  public Hashtable<String,String> multiTapCreateDecodeDictionary(){
      Hashtable <String,String> decodeDictionary = new Hashtable<String,String>();
      decodeDictionary.put("2","A");
      decodeDictionary.put("22","B");
      decodeDictionary.put("222","C");
      decodeDictionary.put("3","D");
      decodeDictionary.put("33","E");
      decodeDictionary.put("333","F");
      decodeDictionary.put("4","G");
      decodeDictionary.put("44","H");
      decodeDictionary.put("444","I");
      decodeDictionary.put("5","J");
      decodeDictionary.put("55","K");
      decodeDictionary.put("555","L");
      decodeDictionary.put("6","M");
      decodeDictionary.put("66","N");
      decodeDictionary.put("666","O");
      decodeDictionary.put("7","P");
      decodeDictionary.put("77","Q");
      decodeDictionary.put("777","R");
      decodeDictionary.put("7777","S");
      decodeDictionary.put("8","T");
      decodeDictionary.put("88","U");
      decodeDictionary.put("888","V");
      decodeDictionary.put("9","W");
      decodeDictionary.put("99","X");
      decodeDictionary.put("999","Y");
      decodeDictionary.put("9999","Z");
      decodeDictionary.put(" "," ");
      return decodeDictionary;
  }
}

class MultiTapCipher{
    public static void main(String args[]){
        MultiTap Obj = new MultiTap();
        String plaintext = "this is the plaintext";
        String ct = Obj.multiTapEncode(plaintext);
        System.out.println(ct);
        System.out.println("After Decoding");
        System.out.println(Obj.multiTapDecode(ct,"-"));
      }
}
