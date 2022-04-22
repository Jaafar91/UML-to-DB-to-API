package com.uda.examples.controller;

import com.uda.examples.service.ExampleService;
import lombok.AllArgsConstructor;
import com.uda.examples.model.*;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@AllArgsConstructor
@RestController
public class ExampleController {

    private final ExampleService exampleService;

    @GetMapping("/example")
    public ResponseEntity<GenericResponse> getAll() {
        return ResponseEntity.ok(exampleService.getAll());
    }

    @GetMapping("/example/{id}")
    public ResponseEntity<GenericResponse> getOne(@PathVariable("id") Integer id) {
        return ResponseEntity.ok(exampleService.getOne(id));
    }

    @PostMapping("/example")
    public ResponseEntity<GenericResponse> createOne(@RequestBody Example example){
        return ResponseEntity.ok(exampleService.createOne(example));
    }

    @DeleteMapping("/example/{id}")
    public ResponseEntity<GenericResponse> deleteOne(@PathVariable("id") Integer id) {
        return ResponseEntity.ok(exampleService.deleteOne(id));
    }

    @PutMapping("/example/{id}")
    public ResponseEntity<GenericResponse> updateOne(@PathVariable("id") Integer id,@RequestBody Example example) {
        return ResponseEntity.ok(exampleService.updateOne(id,example));
    }
}