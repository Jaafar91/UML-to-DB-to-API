package com.uda.examples.mapper;

import com.uda.examples.model.Employee;
import com.uda.examples.entity.EmployeeEntity;
import org.springframework.stereotype.Component;

@Component
public class EmployeeMapper {

    public Employee map(EmployeeEntity employeeEntity) {
        return Employee.builder()
                .id(employeeEntity.getId())
				.first_name(employeeEntity.getFirst_name())
				.last_name(employeeEntity.getLast_name())
				.full_name(employeeEntity.getFull_name())
				.date_of_birth(employeeEntity.getDate_of_birth())
				.active(employeeEntity.getActive())
				.department_id(employeeEntity.getDepartment_id())
                .build();
    }

    public EmployeeEntity map(Employee employee) {
        return EmployeeEntity.builder()
                .id(employee.getId())
				.first_name(employee.getFirst_name())
				.last_name(employee.getLast_name())
				.full_name(employee.getFull_name())
				.date_of_birth(employee.getDate_of_birth())
				.active(employee.getActive())
				.department_id(employee.getDepartment_id())
                .build();
    }
}
