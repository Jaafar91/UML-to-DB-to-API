package com.uda.examples.mapper;

import com.uda.examples.model.Example;
import com.uda.examples.entity.ExampleEntity;
import org.springframework.stereotype.Component;

@Component
public class ExampleMapper {

    public Example map(ExampleEntity exampleEntity) {
        return Example.builder()
                .id(exampleEntity.getId())
				.col1(exampleEntity.getCol1())
				.col2(exampleEntity.getCol2())
                .build();
    }

    public ExampleEntity map(Example example) {
        return ExampleEntity.builder()
                .id(example.getId())
				.col1(example.getCol1())
				.col2(example.getCol2())
                .build();
    }
}
