package com.example.smart_warehouse;

import java.util.List;

import okhttp3.MultipartBody;
import okhttp3.RequestBody;
import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Multipart;
import retrofit2.http.POST;
import retrofit2.http.Part;

public interface Api {

    String BASE_URL = "https://simplifiedcoding.net/demos/";
    String BASE_URL1 = "http://192.168.1.12:5000";
    @GET("marvel")
    Call<List<Results>> getsuperHeroes();

  //  @Multipart
   // @POST("upload")
   // Call<ApiResponse> uploadImage(
    //        @Part MultipartBody.Part image,
    //        @Part("description")RequestBody description
   // );

}
