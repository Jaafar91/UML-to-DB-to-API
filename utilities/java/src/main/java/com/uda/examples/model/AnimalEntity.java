package com.uda.examples.model;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.persistence.Entity;
import javax.persistence.Id;

@Entity(name = "animals")
@Getter
public class AnimalEntity {

    @Id
    private int id;

    private String name;

    private String type;

    private String location;

}
