package com.uda.examples.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class CagesController {

    @GetMapping("/cages")
    public String test() {
        return "hello cages";
    }

}