using System;
using System.Data.SqlClient;
using System.Net;
using System.IO;
using System.Reflection;
using System.Runtime.Serialization.Formatters.Binary;

/*
  Block comment:
  BinaryFormatter bf = new BinaryFormatter();
  bf.Deserialize(fs);
*/

class Test {
    static void Main() {
        // vulnerable: SqlCommand (SQL injection)
        SqlCommand cmd = new SqlCommand("SELECT * FROM Users WHERE name = '" + Console.ReadLine() + "'");

        // vulnerable: ExecuteNonQuery
        cmd.ExecuteNonQuery();

        // vulnerable: ExecuteReader
        var reader = cmd.ExecuteReader();

        // vulnerable: Process.Start
        var p = System.Diagnostics.Process.Start("notepad.exe");

        // vulnerable: HttpWebRequest (potential SSRF)
        HttpWebRequest req = (HttpWebRequest)WebRequest.Create("http://example.com");
        var resp = req.GetResponse();

        // vulnerable: WebClient.DownloadString
        var wc = new WebClient();
        string html = wc.DownloadString("http://example.com");

        // vulnerable: File.ReadAllText (arbitrary file read)
        string secret = File.ReadAllText("secret.txt");

        // vulnerable: Assembly.Load (dynamic code load)
        Assembly asm = Assembly.Load(File.ReadAllBytes("mod.dll"));

        // vulnerable: BinaryFormatter.Deserialize (unsafe deserialization)
        FileStream fs = File.OpenRead("data.bin");
        BinaryFormatter bf = new BinaryFormatter();
        object o = bf.Deserialize(fs);
        fs.Close();

        Console.WriteLine("Finished scan.");
    }
}
