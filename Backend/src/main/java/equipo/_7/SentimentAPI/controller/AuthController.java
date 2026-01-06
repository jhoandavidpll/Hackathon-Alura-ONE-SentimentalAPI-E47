package equipo._7.SentimentAPI.controller;

import equipo._7.SentimentAPI.domain.user.DataAuth;
import equipo._7.SentimentAPI.domain.user.User;
import equipo._7.SentimentAPI.infra.security.DataTokenJWT;
import equipo._7.SentimentAPI.infra.security.TokenService;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/login")
public class AuthController {

    @Autowired
    private TokenService tokenService;
    @Autowired
    private AuthenticationManager manager;

    @PostMapping
    public DataTokenJWT login(@RequestBody @Valid DataAuth data) {
        var authToken = new UsernamePasswordAuthenticationToken(data.email(), data.password());
        var auth = manager.authenticate(authToken);
        var tokenJwt = tokenService.generateToken((User) auth.getPrincipal());
        return new DataTokenJWT(tokenJwt);
    }
}
