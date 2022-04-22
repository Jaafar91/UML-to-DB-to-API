package com.uda.examples.model;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;
import java.util.Date;

@Builder
@Setter
@Getter
public class Example {

    private Integer id;

	private String col1;

	private String col2;
}
