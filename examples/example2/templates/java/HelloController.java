package ${PACKAGE}.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    @GetMapping("/${ROUTE_NAME}")
    public String test() {
        return "hello UDA";
    }

}