package com.uda.examples.controller;

import com.uda.examples.service.EmployeeService;
import lombok.AllArgsConstructor;
import com.uda.examples.model.*;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@AllArgsConstructor
@RestController
public class EmployeeController {

    private final EmployeeService employeeService;

    @GetMapping("/employee")
    public ResponseEntity<GenericResponse> getAll() {
        return ResponseEntity.ok(employeeService.getAll());
    }

    @GetMapping("/employee/{id}")
    public ResponseEntity<GenericResponse> getOne(@PathVariable("id") Integer id) {
        return ResponseEntity.ok(employeeService.getOne(id));
    }

    @PostMapping("/employee")
    public ResponseEntity<GenericResponse> createOne(@RequestBody Employee employee){
        return ResponseEntity.ok(employeeService.createOne(employee));
    }

    @DeleteMapping("/employee/{id}")
    public ResponseEntity<GenericResponse> deleteOne(@PathVariable("id") Integer id) {
        return ResponseEntity.ok(employeeService.deleteOne(id));
    }

    @PutMapping("/employee/{id}")
    public ResponseEntity<GenericResponse> updateOne(@PathVariable("id") Integer id,@RequestBody Employee employee) {
        return ResponseEntity.ok(employeeService.updateOne(id,employee));
    }
}