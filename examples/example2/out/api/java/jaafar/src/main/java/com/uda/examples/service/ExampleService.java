package com.uda.examples.service;

import com.uda.examples.mapper.*;
import com.uda.examples.model.*;
import com.uda.examples.entity.ExampleEntity;
import com.uda.examples.repository.ExampleRepository;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
@AllArgsConstructor
public class ExampleService {

    private final ExampleRepository exampleRepository;
    private final ExampleMapper exampleMapper;
    private final GenericResponseMapper genericResponseMapper;

    public GenericResponse getAll() {
        return genericResponseMapper.map(
            Meta.builder().code("UDAT-1010").message("").build(),
            ExampleData.builder().example(
                exampleRepository.findAll().stream().map(x -> exampleMapper.map(x)).collect(Collectors.toList())
            ).build());
    }

    public GenericResponse getOne(Integer id) {
        return genericResponseMapper.map(
            Meta.builder().code("UDAT-1011").message("").build(),
            exampleMapper.map(
                exampleRepository.findById(id).get()
            ));
    }
    

    public GenericResponse createOne(Example example) {
        exampleRepository.save(exampleMapper.map(example));
        return genericResponseMapper.map(
            Meta.builder().code("UDAT-1012").message("").build(),
            null
            );
    }

    public GenericResponse deleteOne(Integer id) {
        
        exampleRepository.delete(exampleRepository.findById(id).get());
        return genericResponseMapper.map(
            Meta.builder().code("UDAT-1013").message("").build(),
            null);
    }

    public GenericResponse updateOne(Integer id,Example example) {
        
        ExampleEntity exampleEntity=exampleRepository.getById(id);
        if(example.getCol1() != null){
			exampleEntity.setCol1(example.getCol1());
		}
		if(example.getCol2() != null){
			exampleEntity.setCol2(example.getCol2());
		}
        exampleRepository.save(exampleEntity);
        return genericResponseMapper.map(
            Meta.builder().code("UDAT-1014").message("").build(),
            null
            );
    }
}
