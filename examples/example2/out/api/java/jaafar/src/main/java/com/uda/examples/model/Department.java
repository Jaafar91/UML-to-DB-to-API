package com.uda.examples.model;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;
import java.util.Date;

@Builder
@Setter
@Getter
public class Department {

    private Integer id;

	private String name;

	private String location;

	private Integer no_of_offices;
}
