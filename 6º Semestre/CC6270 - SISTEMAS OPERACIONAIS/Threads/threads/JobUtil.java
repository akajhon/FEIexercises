public class JobUtil {

  public static void atrasar(int tempo) {
    try {
      Thread.sleep(tempo * 1000);
    } catch (InterruptedException e) {
      e.printStackTrace();
    }
  }
}
