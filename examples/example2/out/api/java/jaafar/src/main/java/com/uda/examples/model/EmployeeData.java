package com.uda.examples.model;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

import java.util.List;

@Builder
@Setter
@Getter
public class EmployeeData {
    private List<Employee> employee;
}
