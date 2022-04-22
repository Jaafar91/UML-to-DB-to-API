package com.uda.examples.entity;

import lombok.*;
import javax.persistence.Entity;
import javax.persistence.Id;
import java.util.Date;

@Entity(name = "department")
@Setter
@Getter
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class DepartmentEntity {

    @Id
    private Integer id;

    private String name;

	private String location;

	private Integer no_of_offices;

}