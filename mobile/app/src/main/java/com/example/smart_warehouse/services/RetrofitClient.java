package com.example.smart_warehouse.services;
//package io.fututestud.retrofit1.api.service;


import com.example.smart_warehouse.model.ResponseModel;

import retrofit2.Call;
import retrofit2.http.GET;

public interface RetrofitClient {
    @GET("/")
    Call<ResponseModel>getResponseText();


}
