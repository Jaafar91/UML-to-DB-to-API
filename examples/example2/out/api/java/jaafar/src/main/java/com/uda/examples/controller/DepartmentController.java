package com.uda.examples.controller;

import com.uda.examples.service.DepartmentService;
import lombok.AllArgsConstructor;
import com.uda.examples.model.*;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@AllArgsConstructor
@RestController
public class DepartmentController {

    private final DepartmentService departmentService;

    @GetMapping("/department")
    public ResponseEntity<GenericResponse> getAll() {
        return ResponseEntity.ok(departmentService.getAll());
    }

    @GetMapping("/department/{id}")
    public ResponseEntity<GenericResponse> getOne(@PathVariable("id") Integer id) {
        return ResponseEntity.ok(departmentService.getOne(id));
    }

    @PostMapping("/department")
    public ResponseEntity<GenericResponse> createOne(@RequestBody Department department){
        return ResponseEntity.ok(departmentService.createOne(department));
    }

    @DeleteMapping("/department/{id}")
    public ResponseEntity<GenericResponse> deleteOne(@PathVariable("id") Integer id) {
        return ResponseEntity.ok(departmentService.deleteOne(id));
    }

    @PutMapping("/department/{id}")
    public ResponseEntity<GenericResponse> updateOne(@PathVariable("id") Integer id,@RequestBody Department department) {
        return ResponseEntity.ok(departmentService.updateOne(id,department));
    }
}