package com.uda.examples.mapper;

import com.uda.examples.model.Animal;
import com.uda.examples.model.AnimalEntity;
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
