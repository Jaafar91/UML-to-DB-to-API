package ${PACKAGE}.mapper;

import ${PACKAGE}.model.*;
import org.springframework.stereotype.Component;

@Component
public class GenericResponseMapper {

    public GenericResponse map(Meta meta, Object data){
        return GenericResponse.builder()
                .meta(meta)
                .data(data)
                .build();
    }

}