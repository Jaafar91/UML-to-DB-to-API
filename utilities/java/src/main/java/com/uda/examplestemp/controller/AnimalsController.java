package com.uda.examplestemp.controller;

import com.uda.examplestemp.model.Animal;
import com.uda.examplestemp.service.AnimalService;
import lombok.AllArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@AllArgsConstructor
@RestController
public class AnimalsController {

    private final AnimalService animalService;

    @GetMapping("/animals")
    public ResponseEntity<List<Animal>> getAll() {
        return new ResponseEntity<>(animalService.getAll(), HttpStatus.OK);
    }
}