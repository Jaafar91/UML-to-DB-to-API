package com.uda.examples.entity;

import lombok.*;
import javax.persistence.Entity;
import javax.persistence.Id;
import java.util.Date;

@Entity(name = "employee")
@Setter
@Getter
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class EmployeeEntity {

    @Id
    private Integer id;

    private String first_name;

	private String last_name;

	private String full_name;

	private Date date_of_birth;

	private Boolean active;

	private Integer department_id;

}