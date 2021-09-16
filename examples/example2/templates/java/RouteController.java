package ${PACKAGE}.controller;

import ${PACKAGE}.service.${ROUTE_NAME_CAPITALIZE}Service;
import lombok.AllArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.PathVariable;
import ${PACKAGE}.model.GenericResponse;

import java.util.List;

@AllArgsConstructor
@RestController
public class ${ROUTE_NAME_CAPITALIZE}Controller {

    private final ${SINGLE_ROUTE_NAME_CAPITALIZE}Service ${SINGLE_ROUTE_NAME}Service;

    @GetMapping("/${ROUTE_NAME}")
    public ResponseEntity<GenericResponse> getAll() {
        return ResponseEntity.ok(${SINGLE_ROUTE_NAME}Service.getAll());
    }

    @GetMapping("/${ROUTE_NAME}/{${ROUTE_UNIQUE}}")
    public ResponseEntity<GenericResponse> getOne(@PathVariable("${ROUTE_UNIQUE}") int ${ROUTE_UNIQUE}) {
        return ResponseEntity.ok(${SINGLE_ROUTE_NAME}Service.getOne(${ROUTE_UNIQUE}));
    }

}