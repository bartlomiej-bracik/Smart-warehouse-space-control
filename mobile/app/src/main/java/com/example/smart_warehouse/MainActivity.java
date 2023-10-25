package com.example.smart_warehouse;

import androidx.activity.result.contract.ActivityResultContracts;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.os.Debug;
import android.provider.MediaStore;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.Manifest;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    ImageButton cameraButton;
    ImageView image;
    TextView text;
    int CAMERA_PICTURE = 1;

    @SuppressLint({"MissingInflatedId", "WrongViewCast"})
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        findingElementsById();
        cameraButtonListenerMethod();
    }
    void findingElementsById()
    {
        image = findViewById(R.id.image1);
        cameraButton = findViewById(R.id.cameraButton);
        text = findViewById(R.id.textView);
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
    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        if(requestCode == CAMERA_PICTURE && resultCode == RESULT_OK)
        {
            Bitmap picture = (Bitmap) data.getExtras().get("data");
            image.setImageBitmap(picture);
        }
        super.onActivityResult(requestCode, resultCode, data);
    }

}