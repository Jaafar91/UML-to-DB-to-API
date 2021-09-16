package com.uda.examplestemp.mapper;

import com.uda.examplestemp.model.Animal;
import com.uda.examplestemp.model.AnimalEntity;
import org.springframework.stereotype.Component;

@Component
public class AnimalsMapper {

    public Animal map(AnimalEntity animalEntity) {
        return Animal.builder()
                .id(animalEntity.getId())
                .location(animalEntity.getLocation())
                .name(animalEntity.getName())
                .type(animalEntity.getType())
                .build();
    }
}
