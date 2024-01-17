package com.example.smart_warehouse;

import com.google.gson.annotations.SerializedName;

public class ApiResponse {
    @SerializedName("message")
    private String massage;

    public String getMassage()
    {
        return massage;
    }

    public void setMasage(String massage){
        this.massage = massage;
    }

}
