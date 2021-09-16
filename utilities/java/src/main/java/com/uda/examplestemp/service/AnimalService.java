package com.uda.examplestemp.service;

import com.uda.examplestemp.mapper.AnimalsMapper;
import com.uda.examplestemp.model.Animal;
import com.uda.examplestemp.model.AnimalEntity;
import com.uda.examplestemp.repository.AnimalRepository;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
@AllArgsConstructor
public class AnimalService {

    private final AnimalRepository animalRepository;
    private final AnimalsMapper animalsMapper;

    public List<Animal> getAll() {
        List<AnimalEntity> animalEntities = animalRepository.findAll();

        return animalEntities.stream()
                .map(x -> animalsMapper.map(x)).collect(Collectors.toList());
    }
}
