package com.example.smart_warehouse;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.provider.MediaStore;
import android.util.Base64;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.Manifest;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.util.List;

import okhttp3.MediaType;
import okhttp3.RequestBody;
import retrofit2.Call;

//import com.example.smart_warehouse.model.ResponseModel;
//import com.example.smart_warehouse.services.RetrofitClient;

import retrofit2.Callback;
import retrofit2.Response;

public class MainActivity extends AppCompatActivity {

    ListView myList;
    ImageButton cameraButton,infoButton;
    ImageView image;
    TextView text;
    Bitmap imageBitmap;
    String strBase64withImage;

    int CAMERA_PICTURE = 1;

    //private RetrofitClient retrofitClient;

    @SuppressLint({"MissingInflatedId", "WrongViewCast"})
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


       // connectToServer();
        findingElementsById();
        cameraButtonListenerMethod();
        infoButtonListenerMethod();


    }
      void connectToServer()//(View view)
     {
            Call<List<Results>> call = RetrofitClient.getInstance().getMyApi().getsuperHeroes();
        call.enqueue(new Callback<List<Results>>() {
            @Override
            public void onResponse(Call<List<Results>> call, Response<List<Results>> response) {
                List<Results> myHeroList = response.body();
                String[] oneHeroes = new String[myHeroList.size()];

                for(int i = 0 ; i < myHeroList.size();i++){
                    oneHeroes[i] = myHeroList.get(i).getName();
                }

                myList.setAdapter(new ArrayAdapter<String>(getApplicationContext(), android.R.layout.simple_list_item_1, oneHeroes));
            }

            @Override
            public void onFailure(Call<List<Results>> call, Throwable t) {
                Toast.makeText(getApplicationContext(), "An error has occured", Toast.LENGTH_LONG).show();

            }
        });

     }

     void uploadImageOnServer()
     {
         RetrofitClient retrofitClient = RetrofitClient.getInstance();

         String requestData = "{ \"test\": \"test\" }";
         RequestBody requestBody = RequestBody.create(MediaType.parse("application/json"),requestData);
         Call<ApiResponse> call1 = retrofitClient.getMyApi().uploadImage(requestBody);
         try {
             Response<ApiResponse> response = call1.execute();

             if (response.isSuccessful()) {
                 // Sukces - kod 2xx
                 text.setText("Zapytanie POST zostało wysłane bez odpowiedzi");
             } else {
                 // Błąd - obsłuż błędny kod odpowiedzi
                 text.setText("Błąd: " + response.code());
             }
         } catch (IOException e) {
             // Obsłuż błąd wykonania zapytania
             e.printStackTrace();
         }
         /*call1.enqueue(new Callback<ApiResponse>() {
             @Override
             public void onResponse(Call<ApiResponse> call, Response<ApiResponse> response) {
                    text.setText("Działa");
             }

             @Override
             public void onFailure(Call<ApiResponse> call, Throwable t) {
              text.setText(t.getMessage());
             }
         }); */

     }

    public static byte[] bitmapToBytes(Bitmap photo) {
        ByteArrayOutputStream stream = new ByteArrayOutputStream();
        photo.compress(Bitmap.CompressFormat.PNG, 100, stream);
        return stream.toByteArray();
    }

    public static String bytesToBase64(byte[] bytes) {
        final String base64 = Base64.encodeToString(bytes, 0);
        return base64;
    }



    void findingElementsById()
    {
        image = findViewById(R.id.image1);
        cameraButton = findViewById(R.id.cameraButton);
        infoButton = findViewById(R.id.infoButton);
        text = findViewById(R.id.textView);
        myList = (ListView) findViewById(R.id.list);

    }
    private void cameraButtonListenerMethod()
    {
        cameraButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if ( checkSelfPermission(Manifest.permission.CAMERA) == PackageManager.PERMISSION_GRANTED)
                {
                    Intent cameraIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
                    startActivityForResult(cameraIntent,CAMERA_PICTURE);
                }
                else {
                    requestPermissions(new String[]{Manifest.permission.CAMERA},100);
                }
            }
        });
    }

    private void infoButtonListenerMethod()
    {
        infoButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                connectToServer();
            }
        });

    }
    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        if(requestCode == CAMERA_PICTURE && resultCode == RESULT_OK)
        {
            Bitmap picture = (Bitmap) data.getExtras().get("data");
            image.setImageBitmap(picture);

            byte[] bytesImages = bitmapToBytes(picture);
            strBase64withImage = bytesToBase64(bytesImages);
            uploadImageOnServer();


        }
        super.onActivityResult(requestCode, resultCode, data);
    }

}