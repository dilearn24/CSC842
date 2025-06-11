import java.io.*;
import java.text.MessageFormat;
import java.lang.reflect.Method;
import javax.script.ScriptEngineManager;

/* 
  Block comment: examples below should not be flagged
  Runtime.getRuntime().exec("date");
  new ProcessBuilder("cmd", "/c", "dir").start();
*/

public class Test {
    public static void main(String[] args) {
        try {
            // vulnerable: Runtime.exec()
            Runtime.getRuntime().exec("ls -la");

            // vulnerable: ProcessBuilder
            ProcessBuilder pb = new ProcessBuilder("ls", "-la");
            pb.start();

            // vulnerable: ObjectInputStream deserialization
            ObjectInputStream in = new ObjectInputStream(new FileInputStream("data.bin"));
            Object obj = in.readObject();
            in.close();

            // vulnerable: Method.invoke (reflection)
            Method m = String.class.getMethod("toString");
            m.invoke("hello");

            // vulnerable: MessageFormat.format
            String msg = MessageFormat.format("User: {0}", args);

            // vulnerable: String.format
            String sf = String.format("Value: %d", 123);

            // vulnerable: ScriptEngineManager (JS eval)
            ScriptEngineManager sem = new ScriptEngineManager();
            sem.getEngineByName("nashorn").eval("print('hi')");

            // safe alternative (not flagged)
            System.out.println("Done.");

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
