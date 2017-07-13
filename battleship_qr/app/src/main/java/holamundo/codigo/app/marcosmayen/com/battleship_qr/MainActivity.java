package holamundo.codigo.app.marcosmayen.com.battleship_qr;

import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;

import java.io.IOException;

import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "MainActivity";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        new AsyncTask<Void,Void,String>(){


            @Override
            protected String doInBackground(Void... prams){
                OkHttpClient client = new OkHttpClient();
                Request request = new Request.Builder()
                        .url("http://localhost:5000/")
                        .build();
                try {
                    Response response = client.newCall(request).execute();
                    Log.d(TAG,"doInBackground() called with params=["+response.body().string()+"]");
                    System.out.print(response.body().string());
                    return response.body().string();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                return null;
            }
        }.execute();





    }
}
