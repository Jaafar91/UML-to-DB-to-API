package com.uda.examples.service;

import com.uda.examples.mapper.*;
import com.uda.examples.model.*;
import com.uda.examples.entity.EmployeeEntity;
import com.uda.examples.repository.EmployeeRepository;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
@AllArgsConstructor
public class EmployeeService {

    private final EmployeeRepository employeeRepository;
    private final EmployeeMapper employeeMapper;
    private final GenericResponseMapper genericResponseMapper;

    public GenericResponse getAll() {
        return genericResponseMapper.map(
            Meta.builder().code("UDAT-1000").message("").build(),
            EmployeeData.builder().employee(
                employeeRepository.findAll().stream().map(x -> employeeMapper.map(x)).collect(Collectors.toList())
            ).build());
    }

    public GenericResponse getOne(Integer id) {
        return genericResponseMapper.map(
            Meta.builder().code("UDAT-1001").message("").build(),
            employeeMapper.map(
                employeeRepository.findById(id).get()
            ));
    }
    

    public GenericResponse createOne(Employee employee) {
        employeeRepository.save(employeeMapper.map(employee));
        return genericResponseMapper.map(
            Meta.builder().code("UDAT-1002").message("").build(),
            null
            );
    }

    public GenericResponse deleteOne(Integer id) {
        
        employeeRepository.delete(employeeRepository.findById(id).get());
        return genericResponseMapper.map(
            Meta.builder().code("UDAT-1003").message("").build(),
            null);
    }

    public GenericResponse updateOne(Integer id,Employee employee) {
        
        EmployeeEntity employeeEntity=employeeRepository.getById(id);
        if(employee.getFirst_name() != null){
			employeeEntity.setFirst_name(employee.getFirst_name());
		}
		if(employee.getLast_name() != null){
			employeeEntity.setLast_name(employee.getLast_name());
		}
		if(employee.getFull_name() != null){
			employeeEntity.setFull_name(employee.getFull_name());
		}
		if(employee.getDate_of_birth() != null){
			employeeEntity.setDate_of_birth(employee.getDate_of_birth());
		}
		if(employee.getActive() != null){
			employeeEntity.setActive(employee.getActive());
		}
		if(employee.getDepartment_id() != null){
			employeeEntity.setDepartment_id(employee.getDepartment_id());
		}
        employeeRepository.save(employeeEntity);
        return genericResponseMapper.map(
            Meta.builder().code("UDAT-1004").message("").build(),
            null
            );
    }
}
