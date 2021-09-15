package com.uda.examples.service;

import com.uda.examples.mapper.AnimalsMapper;
import com.uda.examples.model.Animal;
import com.uda.examples.model.AnimalEntity;
import com.uda.examples.repository.AnimalRepository;
import lombok.AllArgsConstructor;
import org.graalvm.util.CollectionsUtil;
import org.springframework.stereotype.Service;

import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

@Service
@AllArgsConstructor
public class AnimalService {

    private final AnimalRepository animalRepository;
    private final AnimalsMapper animalsMapper;

    public List<Animal> getAll() {
        List<AnimalEntity> animalEntities =animalRepository.findAll();

        return animalEntities.stream()
                .map(x -> animalsMapper.map(x)).collect(Collectors.toList());
    }
}
