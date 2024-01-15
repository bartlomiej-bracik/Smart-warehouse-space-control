package com.example.smart_warehouse;

import com.google.gson.annotations.SerializedName;

public class Response {

    @SerializedName("responseString")
    private String responseString;

    public Response(String name){
        this.responseString = name;
    }
    public String getResponseString(){
        return responseString;
    }

}
