package com.uda.examples.mapper;

import com.uda.examples.model.Department;
import com.uda.examples.entity.DepartmentEntity;
import org.springframework.stereotype.Component;

@Component
public class DepartmentMapper {

    public Department map(DepartmentEntity departmentEntity) {
        return Department.builder()
                .id(departmentEntity.getId())
				.name(departmentEntity.getName())
				.location(departmentEntity.getLocation())
				.no_of_offices(departmentEntity.getNo_of_offices())
                .build();
    }

    public DepartmentEntity map(Department department) {
        return DepartmentEntity.builder()
                .id(department.getId())
				.name(department.getName())
				.location(department.getLocation())
				.no_of_offices(department.getNo_of_offices())
                .build();
    }
}
