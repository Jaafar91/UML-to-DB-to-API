package com.uda.examples.entity;

import lombok.*;
import javax.persistence.Entity;
import javax.persistence.Id;
import java.util.Date;

@Entity(name = "example")
@Setter
@Getter
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class ExampleEntity {

    @Id
    private Integer id;

    private String col1;

	private String col2;

}