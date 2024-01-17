package com.example.smart_warehouse;

import java.util.List;

import okhttp3.MultipartBody;
import okhttp3.RequestBody;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.Multipart;
import retrofit2.http.POST;
import retrofit2.http.Part;

public interface Api {


    //String BASE_URL3 = "https://bartekbb98.pythonanywhere.com/";
    String BASE_URL = "https://192.168.55.103:5000";


    @POST("upload_mobile")
    Call<ApiResponse> uploadImage(@Body String content );

}
