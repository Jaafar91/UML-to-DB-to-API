package ${PACKAGE}.controller;

import ${PACKAGE}.service.${ROUTE_NAME_CAPITALIZE}Service;
import lombok.AllArgsConstructor;
import com.uda.examples.model.*;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@AllArgsConstructor
@RestController
public class ${ROUTE_NAME_CAPITALIZE}Controller {

    private final ${SINGLE_ROUTE_NAME_CAPITALIZE}Service ${SINGLE_ROUTE_NAME}Service;

    @GetMapping("/${ROUTE_NAME}")
    public ResponseEntity<GenericResponse> getAll() {
        return ResponseEntity.ok(${SINGLE_ROUTE_NAME}Service.getAll());
    }

    @GetMapping("/${ROUTE_NAME}/{${ROUTE_UNIQUE}}")
    public ResponseEntity<GenericResponse> getOne(@PathVariable("${ROUTE_UNIQUE}") ${ROUTE_UNIQUE_DATATYPE} ${ROUTE_UNIQUE}) {
        return ResponseEntity.ok(${SINGLE_ROUTE_NAME}Service.getOne(${ROUTE_UNIQUE}));
    }

    @PostMapping("/${ROUTE_NAME}")
    public ResponseEntity<GenericResponse> createOne(@RequestBody ${SINGLE_ROUTE_NAME_CAPITALIZE} ${SINGLE_ROUTE_NAME}){
        return ResponseEntity.ok(${SINGLE_ROUTE_NAME}Service.createOne(${SINGLE_ROUTE_NAME}));
    }

    @DeleteMapping("/${ROUTE_NAME}/{${ROUTE_UNIQUE}}")
    public ResponseEntity<GenericResponse> deleteOne(@PathVariable("${ROUTE_UNIQUE}") ${ROUTE_UNIQUE_DATATYPE} ${ROUTE_UNIQUE}) {
        return ResponseEntity.ok(${SINGLE_ROUTE_NAME}Service.deleteOne(${ROUTE_UNIQUE}));
    }
}