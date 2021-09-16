package com.uda.examplestemp.model;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

@Builder
@Setter
@Getter
public class Animal {

    private int id;

    private String name;

    private String type;

    private String location;
}
