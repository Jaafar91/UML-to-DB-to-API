package com.uda.examples.controller;

import com.uda.examples.model.Animal;
import com.uda.examples.model.AnimalEntity;
import com.uda.examples.service.AnimalService;
import lombok.AllArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Arrays;
import java.util.List;

@AllArgsConstructor
@RestController
public class AnimalsController {

    private final AnimalService animalService;

    @GetMapping("/animals")
    public ResponseEntity<List<Animal>> getAll() {
        List<Animal> list = animalService.getAll();
        return new ResponseEntity<>(list, HttpStatus.OK);
    }
}