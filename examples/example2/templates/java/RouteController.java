package ${PACKAGE}.controller;

import com.uda.examples.model.${ROUTE_NAME_CAPITALIZE};
import com.uda.examples.service.${ROUTE_NAME_CAPITALIZE}Service;
import lombok.AllArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@AllArgsConstructor
@RestController
public class ${ROUTE_NAME_CAPITALIZE}Controller {

    private final ${SINGLE_ROUTE_NAME_CAPITALIZE}Service ${SINGLE_ROUTE_NAME}Service;

    @GetMapping("/${ROUTE_NAME}")
    public ResponseEntity<List<${SINGLE_ROUTE_NAME_CAPITALIZE}>> getAll() {
        return new ResponseEntity<>(${SINGLE_ROUTE_NAME}Service.getAll(), HttpStatus.OK);
    }

}