package com.uda.examples.model;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;
import java.util.Date;

@Builder
@Setter
@Getter
public class Employee {

    private Integer id;

	private String first_name;

	private String last_name;

	private String full_name;

	private Date date_of_birth;

	private Boolean active;

	private Integer department_id;
}
