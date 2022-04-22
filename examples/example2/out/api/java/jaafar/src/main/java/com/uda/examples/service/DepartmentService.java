package com.uda.examples.service;

import com.uda.examples.mapper.*;
import com.uda.examples.model.*;
import com.uda.examples.entity.DepartmentEntity;
import com.uda.examples.repository.DepartmentRepository;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
@AllArgsConstructor
public class DepartmentService {

    private final DepartmentRepository departmentRepository;
    private final DepartmentMapper departmentMapper;
    private final GenericResponseMapper genericResponseMapper;

    public GenericResponse getAll() {
        return genericResponseMapper.map(
            Meta.builder().code("UDAT-1005").message("").build(),
            DepartmentData.builder().department(
                departmentRepository.findAll().stream().map(x -> departmentMapper.map(x)).collect(Collectors.toList())
            ).build());
    }

    public GenericResponse getOne(Integer id) {
        return genericResponseMapper.map(
            Meta.builder().code("UDAT-1006").message("").build(),
            departmentMapper.map(
                departmentRepository.findById(id).get()
            ));
    }
    

    public GenericResponse createOne(Department department) {
        departmentRepository.save(departmentMapper.map(department));
        return genericResponseMapper.map(
            Meta.builder().code("UDAT-1007").message("").build(),
            null
            );
    }

    public GenericResponse deleteOne(Integer id) {
        
        departmentRepository.delete(departmentRepository.findById(id).get());
        return genericResponseMapper.map(
            Meta.builder().code("UDAT-1008").message("").build(),
            null);
    }

    public GenericResponse updateOne(Integer id,Department department) {
        
        DepartmentEntity departmentEntity=departmentRepository.getById(id);
        if(department.getName() != null){
			departmentEntity.setName(department.getName());
		}
		if(department.getLocation() != null){
			departmentEntity.setLocation(department.getLocation());
		}
		if(department.getNo_of_offices() != null){
			departmentEntity.setNo_of_offices(department.getNo_of_offices());
		}
        departmentRepository.save(departmentEntity);
        return genericResponseMapper.map(
            Meta.builder().code("UDAT-1009").message("").build(),
            null
            );
    }
}
