package com.uda.examples.model;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

@Builder
@Setter
@Getter
public class GenericResponse {
    private Meta meta;
    private Object data;
}
